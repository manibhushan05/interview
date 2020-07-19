//package in.pets.petonix.service;
//
//import in.pets.petonix.filters.GenericPredicate;
//import in.pets.petonix.filters.ParamParser;
//import in.pets.petonix.model.ums.Address;
//import in.pets.petonix.repository.AddressRepository;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.data.domain.Page;
//import org.springframework.data.domain.Pageable;
//import org.springframework.stereotype.Service;
//
//import java.util.Map;
//
//@Service
//public class AddressService {
//    @Autowired
//    AddressRepository addressRepository;
//    public Page<Address> fetchAddress(Map<String, Object> requestParams, Pageable pageable){
//        GenericPredicate genericPredicate = new GenericPredicate(ParamParser.parseParams(requestParams), Address.class);
//        return addressRepository.findAll(genericPredicate.getPredicate(), pageable);
//    }
//}
