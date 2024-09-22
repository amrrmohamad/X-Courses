// Replace with your actual API key from newsapi.org
const apiKey = '7bc5819029f640ca8b6ba28158a090c1';
const newsContainer = document.querySelector('.news-grid');

// Fetch the latest news
async function fetchNews() {
    const url = `https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=${apiKey}`;
    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.status === "ok") {
            displayNews(data.articles);
        } else {
            console.error("Error fetching news:", data.message);
        }
    } catch (error) {
        console.error("Network error:", error);
    }
}

// Function to display the news articles on the website
function displayNews(articles) {
    // Clear the container first
    newsContainer.innerHTML = '';

    // Loop through each article and create the HTML structure for each news item
    articles.forEach(article => {
        const newsItem = document.createElement('div');
        newsItem.classList.add('news-item');

        // Create HTML structure for the news item
        newsItem.innerHTML = `
            <img src="${article.urlToImage || 'placeholder.jpg'}" alt="News Image">
            <h3>${article.title}</h3>
            <p>${article.description || 'No description available.'}</p>
            <a href="${article.url}" target="_blank">Read More</a>
        `;

        // Append the news item to the news grid
        newsContainer.appendChild(newsItem);
    });
}

// Call the fetchNews function when the page loads
window.onload = fetchNews;
