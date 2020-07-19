package in.pets.petonix.filters;

import com.google.common.collect.ImmutableMap;
import com.querydsl.core.BooleanBuilder;
import com.querydsl.core.types.Operator;
import com.querydsl.core.types.Ops;
import com.querydsl.core.types.Predicate;
import com.querydsl.core.types.dsl.Expressions;
import lombok.extern.slf4j.Slf4j;
import org.springframework.util.ReflectionUtils;
import org.springframework.util.StringUtils;

import java.util.List;
import java.util.Map;

@Slf4j
public class GenericPredicate {

    private final List<FieldQueryParameter> parameters;
    private final Class model;

    public GenericPredicate(List<FieldQueryParameter> parameters, Class model) {
        this.parameters = parameters;
        this.model = model;
    }

    static Map<String, Operator> operators = ImmutableMap.<String, Operator>builder()
            .put("::", Ops.STRING_CONTAINS)
            .put("==", Ops.EQ)
            .put("!=", Ops.NE)
            .put(">", Ops.GT)
            .put("<", Ops.LT)
            .put(">=", Ops.GOE)
            .put("<=", Ops.LOE)
            .put("NOT_NULL", Ops.IS_NOT_NULL)
            .put("&&", Ops.AND)
            .put("||", Ops.OR)
            .build();

    public Predicate getPredicate() {

        BooleanBuilder booleanBuilder = new BooleanBuilder();
        parameters
                .forEach(param -> {
                    if (ReflectionUtils.findField(model, param.getFieldKey()) == null) {
                        log.warn("Skipping predicate matching on [%s]. It is not a known field on domainType %s", param, model.getName());
                        return;
                    }
                    if (StringUtils.hasLength(String.valueOf(param.getFieldValue()))) {
                        if (StringUtils.hasLength(String.valueOf(param.getFieldCondition()))) {
                            if (String.valueOf(param.getFieldCondition()).equalsIgnoreCase("||")) {
                                booleanBuilder.or(matchesProperty(param, model));
                            } else {
                                booleanBuilder.and(matchesProperty(param, model));
                            }
                        } else {
                            booleanBuilder.and(matchesProperty(param, model));
                        }
                    }
                });

        log.debug("Boolean builder value : {}", booleanBuilder.getValue());
        return booleanBuilder;
    }

    private Predicate matchesProperty(FieldQueryParameter param, Class<?> model) {
        return Expressions.predicate(operators.get(param.getFieldOperator()), Expressions.path(model, param.getFieldKey()), Expressions.constant(param.getFieldValue()));
    }
}