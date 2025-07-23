using System.ComponentModel.DataAnnotations; // To use [Required].
using System.ComponentModel.DataAnnotations.Schema; // To use [Column].
namespace Northwind.EntityModels;
public class Product
{
    //We don't need to include all columns from a table as properties!
    //When making a new row those columns will be null or some other default value
    //So make sure those columns are optional or have a default value!

    //We only map six properties since we have decided we don't need the rest!

    //The two properties that relate the two entities, Category.Products and
    //Product.Category, are both marked as virtual. This allows EF Core to
    //inherit and override the properties to provide extra features, such as lazy loading.
    


    // The primary key.
    public int ProductId { get; set; } 

    //Every string must have 40 characters
    [Required]
    [StringLength(40)]
    
    public string ProductName { get; set; } = null!;
    
    // Property name is different from the column name.
    [Column("UnitPrice", TypeName = "money")]
    
    public decimal? Cost { get; set; }
    [Column("UnitsInStock")]
    
    public short? Stock { get; set; }
    public bool Discontinued { get; set; }
    
    // These two properties define the foreign key relationship
    // to the Categories table.
    public int CategoryId { get; set; }
    public virtual Category Category { get; set; } = null!;
}   
    