package in.pets.petonix.model.ums;

import com.fasterxml.jackson.databind.PropertyNamingStrategy;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Getter
@Setter
@NoArgsConstructor
@Table(name = "users")
@Entity
@JsonNaming(PropertyNamingStrategy.SnakeCaseStrategy.class)
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private String id;

    private String password;

    private String firstName;

    private String lastName;

    private String mobileNumber;
}
