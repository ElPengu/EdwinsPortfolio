using Microsoft.AspNetCore.Mvc;

namespace ASPNETPRACTISE_EDWIN.Controllers
{
    public class NorthwindController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
