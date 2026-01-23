package ec.edu.ups.icc.fundamentos01.products.dtos;

import java.util.List;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

/**
 * DTO para respuestas de paginación usando Slice
 * Sin totalElements ni totalPages (más ligero que Page)
 */
@JsonPropertyOrder({
        "content",
        "empty",
        "first",
        "last",
        "number",
        "numberOfElements",
        "size",
        "sort"
})
public class SliceResponseDto {
    public List<ProductResponseDto> content;
    public boolean empty;
    public boolean first;
    public boolean last;
    public int number;
    public int numberOfElements;
    public int size;
    public SortDto sort;

    @JsonPropertyOrder({"empty", "sorted", "unsorted"})
    public static class SortDto {
        public boolean empty;
        public boolean sorted;
        public boolean unsorted;
    }
}
