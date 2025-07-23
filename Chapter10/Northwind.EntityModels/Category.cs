using System.ComponentModel.DataAnnotations.Schema; //To use [Column]
namespace Northwind.EntityModels;


public class Category
{
    //These properties map to columns in the database

    //The primary key
    public int CategoryId { get; set; } 

    // Category name does not allow nulls
    public string CategoryName { get; set; } = null!;

    //The description allows ntext, not normal nvarchar
    [Column(TypeName = "ntext")]
    public string? Description { get; set; }

    // Defines a navigation property for related rows.
    public virtual ICollection<Product> Products { get; set; }
      // To enable developers to add products to a Category, we must
      // initialize the navigation property to an empty collection.
      // This also avoids an exception if we get a member like Count.
      = new HashSet<Product>();

}


/*Here we define the entity model for the 
 categories table

 In the Northwind4SQLite.sql file it looks 
like this

 CREATE TABLE Categories (
  CategoryId   INTEGER       PRIMARY KEY,
  CategoryName NVARCHAR (15) NOT NULL,
  Description  "NTEXT",
  Picture      "IMAGE"
);
*/