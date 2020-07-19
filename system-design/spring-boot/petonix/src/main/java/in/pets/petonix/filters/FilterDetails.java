package in.pets.petonix.filters;

import lombok.Getter;
import lombok.Setter;

import java.io.Serializable;
import java.util.List;

@Getter
@Setter
public class FilterDetails implements Serializable {

    private List<FieldQueryParameter> filterFieldParams;
}