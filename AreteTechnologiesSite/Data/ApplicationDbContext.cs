using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;
using AreteTechnologiesSite.Models;

namespace AreteTechnologiesSite.Data
{
    public class ApplicationDbContext : IdentityDbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }
        public DbSet<AreteTechnologiesSite.Models.Joke> Joke { get; set; } = default!;
        public DbSet<AreteTechnologiesSite.Models.Article> Article { get; set; } = default!;
        public DbSet<AreteTechnologiesSite.Models.Scrum_Product> Scrum_Product { get; set; } = default!;
    }
}
