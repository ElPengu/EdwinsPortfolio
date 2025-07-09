using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace AreteTechnologiesSite.Data.Migrations
{
    /// <inheritdoc />
    public partial class initialsetupScrumProduct : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Scrum_Product",
                columns: table => new
                {
                    Id = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    ProductTitle = table.Column<string>(type: "nvarchar(max)", nullable: false),
                    ProductVision = table.Column<string>(type: "nvarchar(max)", nullable: false),
                    ProductEpic = table.Column<string>(type: "nvarchar(max)", nullable: false),
                    ProductStory = table.Column<string>(type: "nvarchar(max)", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Scrum_Product", x => x.Id);
                });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Scrum_Product");
        }
    }
}
