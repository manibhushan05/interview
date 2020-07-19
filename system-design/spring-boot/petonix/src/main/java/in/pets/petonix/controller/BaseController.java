package in.pets.petonix.controller;

import org.apache.commons.lang3.StringUtils;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

import javax.servlet.http.HttpServletRequest;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class BaseController {
    public Pageable getPaginationAndSortingParams(HttpServletRequest request) {
        String pageParam = request.getParameter("page");
        String sizeParam = request.getParameter("size");
        String sortParam = request.getParameter("sort");

        int page = !StringUtils.isBlank(pageParam) ? (Integer.parseInt(pageParam.trim())-1) : 0;
        int size = !StringUtils.isBlank(sizeParam) ? Integer.parseInt(sizeParam.trim()) : 10;

        Sort sort = fetchOrSetDefaultSort(sortParam);
        Pageable pageable = PageRequest.of(page, size, sort);

        return pageable;
    }

    public Map<String, Object> getPaginatedContent(Page pagedContent){
        Map<String, Object> mapper = new HashMap<String, Object>();
        if(pagedContent.hasContent()) {
            mapper.put("content", pagedContent.getContent());
        } else {
            mapper.put("content", new ArrayList<Object>());
        }

        mapper.put("currentPage", pagedContent.getNumber()+1);
        mapper.put("totalItems", pagedContent.getTotalElements());
        mapper.put("totalPages", pagedContent.getTotalPages());

        return mapper;
    }

    private Sort fetchOrSetDefaultSort(String sortParam) {
        String[] sortParams = StringUtils.isBlank(sortParam) ? " ".split(",") : sortParam.split(",");
        String sortByParam = sortParams.length>0 ? sortParams[0].trim() : "";
        String orderParam = sortParams.length>1 ? sortParams[1].trim() : "ASC";

        String sortBy = !StringUtils.isBlank(sortByParam) ? sortByParam : "id";
        String order = !StringUtils.isBlank(orderParam) ? orderParam : "ASC";

        return (order.toUpperCase().equals("DESC") ? Sort.by(sortBy).descending() : Sort.by(sortBy).ascending());
    }
}
