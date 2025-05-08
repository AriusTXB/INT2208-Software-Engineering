fetch('../../Database/data.json')
  .then(response => response.json())
  .then(news => {
    function loadNews(mainId, sideId) {
      const mainArticleContainer = document.getElementById(mainId);
      const sideArticlesContainer = document.getElementById(sideId);

      // Bài báo chính có ảnh
      const mainArticle = news.find(article => article.image !== "");
      if (mainArticle) {
        const mainArticleHTML = `
          <img src="${mainArticle.image}" alt="${mainArticle.title}">
          <div class="article-content">
            <h3><a href="article.html">${mainArticle.title}</a></h3>
            <p class="article-meta">By ${mainArticle.author} • ${mainArticle.date}</p>
            <p>${mainArticle.description}</p>
          </div>
        `;
        mainArticleContainer.innerHTML = mainArticleHTML;
      }

      // Các bài báo phụ không có ảnh
      const sideArticles = news.filter(article => article.image === "");
      sideArticles.forEach(article => {
        const authorHTML = article.author ? `<p class="article-author">By ${article.author}</p>` : '';
        const sideArticleHTML = `
          <article>
            <h4><a href="article.html">${article.title}</a></h4>
            ${authorHTML}
            <p class="article-meta">${article.date}</p>
          </article>
        `;
        sideArticlesContainer.innerHTML += sideArticleHTML;
      });
    }

    // Loading Breaking News
    loadNews('main-article-breaking', 'side-articles-breaking');

    // Loading Latest News
    loadNews('main-article-latest', 'side-articles-latest');

    //Loading Trending News
    loadNews('main-article-trending', 'side-articles-trending');
  })
  .catch(err => console.error("Error loading data:", err));
