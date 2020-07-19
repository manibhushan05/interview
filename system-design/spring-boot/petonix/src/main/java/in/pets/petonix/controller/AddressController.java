package in.pets.petonix.controller;

import in.pets.petonix.model.ums.Address;
import in.pets.petonix.repository.AddressRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "/")
public class AddressController extends BaseController {
    @Autowired
    AddressRepository addressRepository;

//    @Autowired
//    AddressService addressService;

    @PostMapping("address")
    public ResponseEntity<Address> createAdress(@RequestBody Address address) {
        Address addressData = addressRepository.save(address);
        return new ResponseEntity<>(addressData, HttpStatus.CREATED);
    }
//    @GetMapping(value = "address")
//    public ResponseEntity<Map<String, Object>>  getAddress(@RequestParam Map<String, Object> requestParams,
//                                                           HttpServletRequest request) {
//
//        Map responseMapper;
//        Pageable pageable = getPaginationAndSortingParams(request);
//        Page<Address> addresses = addressService.fetchAddress(requestParams, pageable);
//        responseMapper = getPaginatedContent(addresses);
//
//        return new ResponseEntity<>(responseMapper, HttpStatus.OK);
//    }
}
