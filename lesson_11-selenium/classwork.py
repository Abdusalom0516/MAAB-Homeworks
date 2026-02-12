# from bs4 import BeautifulSoup

# hyml_txt = ''''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Bookstore Demo Page</title>
#     <meta name="description" content="A fake bookstore page for scraping practice">
# </head>
# <body>

# <header>
#     <h1>📚 The Scrapy Bookstore</h1>
#     <nav>
#         <ul>
#             <li><a href="/home">Home</a></li>
#             <li><a href="/books">Books</a></li>
#             <li><a href="/contact">Contact</a></li>
#         </ul>
#     </nav>
# </header>

# <main>
#     <section id="featured">
#         <h2>Featured Books</h2>

#         <div class="book" data-id="bk101">
#             <h3 class="title">Python for Beginners</h3>
#             <p class="author">By Alice Johnson</p>
#             <p class="price">$29.99</p>
#             <p class="rating" data-stars="4.5">★★★★☆</p>
#             <a href="/books/python-for-beginners">View details</a>
#         </div>

#         <div class="book out-of-stock" data-id="bk102">
#             <h3 class="title">Advanced Web Scraping</h3>
#             <p class="author">By Bob Smith</p>
#             <p class="price">$39.50</p>
#             <p class="rating" data-stars="4.8">★★★★★</p>
#             <span class="status">Out of stock</span>
#         </div>

#         <div class="book" data-id="bk103">
#             <h3 class="title">Data Science with Python</h3>
#             <p class="author">By Carol Lee</p>
#             <p class="price">$45.00</p>
#             <!-- rating missing on purpose -->
#             <a href="/books/data-science-python">View details</a>
#         </div>
#     </section>

#     <section id="categories">
#         <h2>Categories</h2>
#         <ul>
#             <li data-count="12">Programming</li>
#             <li data-count="7">Data Science</li>
#             <li data-count="5">Web Development</li>
#         </ul>
#     </section>

#     <section id="customers">
#         <h2>Recent Customers</h2>
#         <table border="1">
#             <thead>
#                 <tr>
#                     <th>Name</th>
#                     <th>Country</th>
#                     <th>Books Purchased</th>
#                 </tr>
#             </thead>
#             <tbody>
#                 <tr>
#                     <td>John Doe</td>
#                     <td>USA</td>
#                     <td>3</td>
#                 </tr>
#                 <tr>
#                     <td>Maria García</td>
#                     <td>Spain</td>
#                     <td>1</td>
#                 </tr>
#                 <tr>
#                     <td>Wei Chen</td>
#                     <td>China</td>
#                     <td>5</td>
#                 </tr>
#             </tbody>
#         </table>
#     </section>
# </main>

# <footer>
#     <p>&copy; 2026 The Scrapy Bookstore</p>
#     <p class="hidden" style="display:none;">Internal code: XJ92-KL</p>
# </footer>

# </body>
# </html>
# '''

# soup = BeautifulSoup(hyml_txt, "html.parser")

# th = soup.th

# print(th.name)
# print(th.text)
# print(th.string)

# allThs = soup.find_all("th")
# print(allThs)

# liWithDataCount7 = soup.find(id="pricing")
# print(liWithDataCount7)




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
# chrome_options.add_argument("--headless") # Works but does not open the browser
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)

driver.get("https://google.com/")
print("Headless mode page title: ", driver.title)

search_box = driver.find_element(by=By.CLASS_NAME, value="gLFyf")

search_box.send_keys("Vinland Saga Season 3", Keys.RETURN)


# driver.quit()
