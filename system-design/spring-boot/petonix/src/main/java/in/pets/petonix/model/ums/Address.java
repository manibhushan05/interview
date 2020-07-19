//package in.pets.petonix.model.ums;
//
//import com.fasterxml.jackson.databind.PropertyNamingStrategy;
//import com.fasterxml.jackson.databind.annotation.JsonNaming;
//import lombok.Getter;
//import lombok.Setter;
//import org.springframework.data.annotation.Id;
//import org.springframework.data.mongodb.core.mapping.Document;
//
//import javax.validation.constraints.NotBlank;
//import javax.validation.constraints.NotNull;
//
//@Getter
//@Setter
//@Document(collection = "address")
//@JsonNaming(PropertyNamingStrategy.SnakeCaseStrategy.class)
//public class Address {
//    @Id
//    private String id;
//    private String streetAddress;
//
//    @NotNull
//    @NotBlank
//    private String city;
//
//    @NotNull
//    @NotBlank
//    private String pinCode;
//
//    private String state;
//
//    @NotNull
//    private String country;
//}
