using Microsoft.EntityFrameworkCore; // To use DbContext and so on.

// To use RelationalEventId.
using Microsoft.EntityFrameworkCore.Diagnostics;

namespace Northwind.EntityModels;
// This manages interactions with the Northwind database.
public class NorthwindDb : DbContext
{
    // These two properties map to tables in the database.
    public DbSet<Category>? Categories { get; set; }
    public DbSet<Product>? Products { get; set; }

    protected override void OnConfiguring(
      DbContextOptionsBuilder optionsBuilder)
    {
        string databaseFile = "Northwind.db";
        string path = Path.Combine(
          Environment.CurrentDirectory, databaseFile);
        string connectionString = $"Data Source={path}";
        WriteLine($"Connection: {connectionString}");
        optionsBuilder.UseSqlite(connectionString);

        /*
         Statements to log to the console and include
         sensitive data like parameter values for commands 
         sent to the database IF we compile the debug config
         */
        /*
         NOTE: When we are in release more the lines 
        within the IF ENDIF section are greyed out, 
        else they are not!
         */
        optionsBuilder.LogTo(WriteLine, // This is the Console method.
        // To only view the log information for LINQ queries 
        // being translated to SQL statements and their execution, 
        // we need the following line. 
        // Note that the book states that in this 
        // instance the event ID to output has an Id value
        // of 20100
        new[] { RelationalEventId.CommandExecuting }) 
        
        #if DEBUG
          .EnableSensitiveDataLogging() // Include SQL parameters.
          .EnableDetailedErrors()
        #endif
        ;

    }
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        {
            // Example of using Fluent API instead of attributes
            // to limit the length of a category name to 15.
            modelBuilder.Entity<Category>()
              .Property(category => category.CategoryName)
              .IsRequired() // NOT NULL
              .HasMaxLength(15);
            // Some SQLite-specific configuration.
            if (Database.ProviderName?.Contains("Sqlite") ?? false)
            {
                // To "fix" the lack of decimal support in SQLite.
                modelBuilder.Entity<Product>()
                  .Property(product => product.Cost)
                  .HasConversion<double>();
            }
        }

        // A global filter to remove discontinued products.
        modelBuilder.Entity<Product>()
          .HasQueryFilter(p => !p.Discontinued);
    }
}