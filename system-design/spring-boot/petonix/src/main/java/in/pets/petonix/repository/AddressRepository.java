package in.pets.petonix.repository;

import in.pets.petonix.model.ums.Address;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AddressRepository  extends MongoRepository<Address, String> {
}
