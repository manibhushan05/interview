package in.pets.petonix.filters;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class ParamParser {
    public static List<FieldQueryParameter> parseParams(Map<String, Object> requestParams) {
        List<FieldQueryParameter> fieldQueryParameters = new ArrayList<>();

        for (String key : requestParams.keySet()) {
            if (requestParams.getOrDefault(key, null) != null) {
                FieldQueryParameter fieldQueryParameter = new FieldQueryParameter();
                fieldQueryParameter.setFieldKey(key);
                fieldQueryParameter.setFieldValue(requestParams.get(key));
                fieldQueryParameter.setFieldOperator("==");
                fieldQueryParameters.add(fieldQueryParameter);
            }
        }
        return fieldQueryParameters;
    }
}
