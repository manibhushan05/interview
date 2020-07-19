package in.pets.petonix.service;

import in.pets.petonix.filters.GenericPredicate;
import in.pets.petonix.filters.ParamParser;
import in.pets.petonix.model.ums.QUser;
import in.pets.petonix.model.ums.User;
import in.pets.petonix.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.Map;

@Service
public class FetchUserService {
    @Autowired
    UserRepository userRepository;
    public Page<User> fetchUsers(Map<String, Object> requestParams, Pageable pageable){
        GenericPredicate genericPredicate = new GenericPredicate(ParamParser.parseParams(requestParams), QUser.class);
        return userRepository.findAll(genericPredicate.getPredicate(), pageable);
    }
}
