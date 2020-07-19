package in.pets.petonix.controller;

import in.pets.petonix.model.ums.User;
import in.pets.petonix.repository.UserRepository;
import in.pets.petonix.service.FetchUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.Map;

@RestController
@RequestMapping(value = "/")
public class UserController extends BaseController {
    @Autowired
    UserRepository userRepository;

    @Autowired
    FetchUserService fetchUserService;

    @PostMapping("users")
    public ResponseEntity<User> createUser(@RequestBody User user) {
        User userData = userRepository.save(user);
        return new ResponseEntity<>(userData, HttpStatus.CREATED);
    }

    @GetMapping(value = "users")
    public ResponseEntity<Map<String, Object>>  getUsers(@RequestParam Map<String, Object> requestParams,
                                HttpServletRequest request) {

        Map responseMapper;
        Pageable pageable = getPaginationAndSortingParams(request);
        Page<User> userList = fetchUserService.fetchUsers(requestParams, pageable);
        responseMapper = getPaginatedContent(userList);

        return new ResponseEntity<>(responseMapper, HttpStatus.OK);
    }
}
