using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using AreteTechnologiesSite.Data;
using AreteTechnologiesSite.Models;

namespace AreteTechnologiesSite.Controllers
{
    public class Scrum_ProductController : Controller
    {
        private readonly ApplicationDbContext _context;

        public Scrum_ProductController(ApplicationDbContext context)
        {
            _context = context;
        }

        // GET: Scrum_Product
        public async Task<IActionResult> Index()
        {
            return View(await _context.Scrum_Product.ToListAsync());
        }

        // GET: Scrum_Product/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var scrum_Product = await _context.Scrum_Product
                .FirstOrDefaultAsync(m => m.Id == id);
            if (scrum_Product == null)
            {
                return NotFound();
            }

            return View(scrum_Product);
        }

        // GET: Scrum_Product/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Scrum_Product/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,ProductTitle,ProductVision,ProductEpic,ProductStory")] Scrum_Product scrum_Product)
        {
            if (ModelState.IsValid)
            {
                _context.Add(scrum_Product);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }
            return View(scrum_Product);
        }

        // GET: Scrum_Product/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var scrum_Product = await _context.Scrum_Product.FindAsync(id);
            if (scrum_Product == null)
            {
                return NotFound();
            }
            return View(scrum_Product);
        }

        // POST: Scrum_Product/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,ProductTitle,ProductVision,ProductEpic,ProductStory")] Scrum_Product scrum_Product)
        {
            if (id != scrum_Product.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(scrum_Product);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!Scrum_ProductExists(scrum_Product.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }
            return View(scrum_Product);
        }

        // GET: Scrum_Product/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var scrum_Product = await _context.Scrum_Product
                .FirstOrDefaultAsync(m => m.Id == id);
            if (scrum_Product == null)
            {
                return NotFound();
            }

            return View(scrum_Product);
        }

        // POST: Scrum_Product/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var scrum_Product = await _context.Scrum_Product.FindAsync(id);
            if (scrum_Product != null)
            {
                _context.Scrum_Product.Remove(scrum_Product);
            }

            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }

        private bool Scrum_ProductExists(int id)
        {
            return _context.Scrum_Product.Any(e => e.Id == id);
        }
    }
}
