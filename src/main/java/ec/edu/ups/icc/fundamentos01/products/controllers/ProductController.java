package ec.edu.ups.icc.fundamentos01.products.controllers;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Slice;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import ec.edu.ups.icc.fundamentos01.products.dtos.CreateProductDto;
import ec.edu.ups.icc.fundamentos01.products.dtos.UpdateProductDto;
import ec.edu.ups.icc.fundamentos01.products.dtos.ProductResponseDto;
import ec.edu.ups.icc.fundamentos01.products.dtos.SliceResponseDto;
import ec.edu.ups.icc.fundamentos01.products.services.ProductService;
import jakarta.validation.Valid;

@RestController
@RequestMapping("/api/products")
public class ProductController {

    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @PostMapping
    public ResponseEntity<ProductResponseDto> create(@Valid @RequestBody CreateProductDto dto) {
        ProductResponseDto created = productService.create(dto);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    @GetMapping("/{id}")
    public ResponseEntity<ProductResponseDto> findById(@PathVariable("id") String id) {
        ProductResponseDto product = productService.findById(Long.parseLong(id));
        return ResponseEntity.ok(product);
    }

    @PutMapping("/{id}")
    public ResponseEntity<ProductResponseDto> update(
            @PathVariable("id") Long id,
            @Valid @RequestBody UpdateProductDto dto) {
        ProductResponseDto updated = productService.update(id, dto);
        return ResponseEntity.ok(updated);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable("id") Long id) {
        productService.delete(id);
        return ResponseEntity.noContent().build();
    }

    // ============== PAGINACIÓN BÁSICA (RAÍZ) ==============
    @GetMapping
    public ResponseEntity<Page<ProductResponseDto>> list(
            @RequestParam(name = "page", defaultValue = "0") int page,
            @RequestParam(name = "size", defaultValue = "10") int size,
            @RequestParam(name = "sort", defaultValue = "id") String[] sort) {

        Page<ProductResponseDto> products = productService.findAll(page, size, sort);
        return ResponseEntity.ok(products);
    }

// ============== PAGINACIÓN CON FILTROS ==============
@GetMapping("/search")
public ResponseEntity<Page<ProductResponseDto>> findWithFilters(
        @RequestParam(name = "name", required = false) String name,
        @RequestParam(name = "minPrice", required = false) Double minPrice,
        @RequestParam(name = "maxPrice", required = false) Double maxPrice,
        @RequestParam(name = "categoryId", required = false) Long categoryId,
        @RequestParam(name = "page", defaultValue = "0") int page,
        @RequestParam(name = "size", defaultValue = "10") int size,
        @RequestParam(name = "sort", defaultValue = "createdAt") String[] sort) {

    Page<ProductResponseDto> products = productService.findWithFilters(
            name, minPrice, maxPrice, categoryId, page, size, sort);

    return ResponseEntity.ok(products);
}

// ============== PAGINACIÓN CON SLICE ==============
@GetMapping("/slice")
public ResponseEntity<SliceResponseDto> findAllSlice(
        @RequestParam(name = "page", defaultValue = "0") int page,
        @RequestParam(name = "size", defaultValue = "10") int size,
        @RequestParam(name = "sort", defaultValue = "id") String[] sort) {

    Slice<ProductResponseDto> products = productService.findAllSlice(page, size, sort);
    SliceResponseDto response = toSliceResponseDto(products);
    return ResponseEntity.ok(response);
}

// ============== PRODUCTOS POR CATEGORÍA ==============
@GetMapping("/category/{categoryId}")
public ResponseEntity<Page<ProductResponseDto>> findByCategoryId(
        @PathVariable("categoryId") Long categoryId,
        @RequestParam(name = "page", defaultValue = "0") int page,
        @RequestParam(name = "size", defaultValue = "10") int size,
        @RequestParam(name = "sort", defaultValue = "id") String[] sort) {

    Page<ProductResponseDto> products = productService.findByCategoryId(categoryId, page, size, sort);
    return ResponseEntity.ok(products);
}

// ============== PRODUCTOS POR USUARIO ==============
@GetMapping("/user/{userId}")
public ResponseEntity<Page<ProductResponseDto>> findByUserId(
        @PathVariable("userId") Long userId, // <-- IMPORTANTE
        @RequestParam(name = "name", required = false) String name,
        @RequestParam(name = "minPrice", required = false) Double minPrice,
        @RequestParam(name = "maxPrice", required = false) Double maxPrice,
        @RequestParam(name = "categoryId", required = false) Long categoryId,
        @RequestParam(name = "page", defaultValue = "0") int page,
        @RequestParam(name = "size", defaultValue = "10") int size,
        @RequestParam(name = "sort", defaultValue = "createdAt") String[] sort) {

    Page<ProductResponseDto> products = productService.findByUserIdWithFilters(
            userId, name, minPrice, maxPrice, categoryId, page, size, sort);

    return ResponseEntity.ok(products);
}

// ============== MÉTODOS HELPERS ==============

private SliceResponseDto toSliceResponseDto(Slice<ProductResponseDto> slice) {
    SliceResponseDto response = new SliceResponseDto();
    response.content = slice.getContent();
    response.empty = slice.isEmpty();
    response.first = slice.isFirst();
    response.last = slice.isLast();
    response.number = slice.getNumber();
    response.numberOfElements = slice.getNumberOfElements();
    response.size = slice.getSize();
    
    SliceResponseDto.SortDto sortDto = new SliceResponseDto.SortDto();
    sortDto.empty = slice.getSort().isEmpty();
    sortDto.sorted = slice.getSort().isSorted();
    sortDto.unsorted = !slice.getSort().isSorted();
    response.sort = sortDto;
    
    return response;
}

}