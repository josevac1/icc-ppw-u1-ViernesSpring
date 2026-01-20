package ec.edu.ups.icc.fundamentos01.products.services;

import java.util.List;

import org.springframework.boot.data.autoconfigure.web.DataWebProperties.Pageable;
import org.springframework.data.domain.Page;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import ec.edu.ups.icc.fundamentos01.products.dtos.CreateProductDto;

import ec.edu.ups.icc.fundamentos01.products.dtos.UpdateProductDto;
import ec.edu.ups.icc.fundamentos01.products.models.ProductEntity;
import ec.edu.ups.icc.fundamentos01.products.dtos.ProductResponseDto;

public interface ProductService {

    ProductResponseDto create(CreateProductDto dto);

    List<ProductResponseDto> findAll();
    
    Page<ProductResponseDto> findAll(int page, int size, String[] sort);

    ProductResponseDto findById(Long id);

    List<ProductResponseDto> findByUserId(Long id);

    List<ProductResponseDto> findByCategoryId(Long id);

    ProductResponseDto update(Long id, UpdateProductDto dto);

    void delete(Long id);

    Page<ProductResponseDto> findAllPaginado(int page, int size, String[] sort);

}
