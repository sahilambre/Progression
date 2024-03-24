const apiKey = "bc0892fba6aa42ffbb5eda4bacfc1ae9";

const blogContainer = document.getElementById("blog-container");

const searchField = document.getElementById("search-input");

const searchButton = document.getElementById("search-button");

async function fetchRandomNews() {
  try {
    const apiUrl = `https://newsapi.org/v2/top-headlines?country=us&pageSize=20&apikey=${apiKey}`;
    const response = await fetch(apiUrl);
    const data = await response.json();
    // console.log(data);
    return data.articles;
  } catch (error) {
    console.error("error fetching random news!", error);
    return [];
  }
}

// !  search functionality

// searchButton.addEventListener("click", async () => {
//   //   const query = searchField.ariaValueMax.trim();
//   const query = searchField.trim();

//   if (query !== " ") {
//     try {
//       const articles = await fetchNewsQuery(query);
//       displayBlogs(articles);
//     } catch (error) {
//       console.log("error fetching news by query", error);
//     }
//   }
// });

searchButton.addEventListener("click", async () => {
  //   console.log(searchField.value);
  const query = searchField.value.trim(); // Corrected variable usage
  console.log(query);
  if (query !== "") {
    // Corrected empty string comparison

    try {
      const articles = await fetchNewsQuery(query);
      displayBlogs(articles);
    } catch (error) {
      console.log("error fetching news by query", error);
    }
  }
});

async function fetchNewsQuery(query) {
  try {
    const apiUrl = `https://newsapi.org/v2/everything?q=${query}&pageSize=10&apikey=${apiKey}`;
    const response = await fetch(apiUrl);
    const data = await response.json();
    // console.log(data);
    return data.articles;
  } catch (error) {
    console.error("error fetching random news!", error);
    return [];
  }
}

function displayBlogs(articles) {
  blogContainer.innerHTML = "";
  articles.forEach((article) => {
    const blogCard = document.createElement("div");
    blogCard.classList.add("blog-card");

    const img = document.createElement("img");
    img.src = article.urlToImage;
    img.alt = article.title;

    const title = document.createElement("h2");
    // title.textContent = article.title;
    const truncatedTitle =
      article.title.length > 30
        ? article.title.slice(0, 30) + "....."
        : article.title;

    title.textContent = truncatedTitle;

    const description = document.createElement("p");
    // description.textContent = article.description;
    const truncatedDescription =
      article.description.length > 120
        ? article.description.slice(0, 120) + "....."
        : article.description;

    description.textContent = truncatedDescription;

    blogCard.appendChild(img);
    blogCard.appendChild(title);
    blogCard.appendChild(description);
    blogCard.addEventListener("click", () => {
      window.open(article.url, "_blank");
    });
    blogContainer.appendChild(blogCard);
  });
}

(async () => {
  try {
    const articles = await fetchRandomNews();
    // console.log(articles);
    displayBlogs(articles);
  } catch (error) {
    console.error("error fetching random news!", error);
  }
})();
