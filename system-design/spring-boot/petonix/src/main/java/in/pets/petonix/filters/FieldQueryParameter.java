package in.pets.petonix.filters;

import lombok.Getter;
import lombok.Setter;

import java.io.Serializable;

@Getter
@Setter
public class FieldQueryParameter implements Serializable {

    //column name
    private String fieldKey;
    //column value
    private Object fieldValue;
    /*
    and, or
     */
    private String fieldCondition;
    // like and order
    private String fieldOperator;
}