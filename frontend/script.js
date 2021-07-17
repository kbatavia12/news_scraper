var newsNumber = 1

const fetchNews = async (i) => {
    const res = await fetch(`https://news-scraper-project.herokuapp.com/get-news?number=${i}`).then(res => res.json());
    return res;
}

const createComponent = (newsTitle, newsDate, newsDescription) => {
    const parent = document.createElement('div');
    parent.classList.add('news');
    const heading = document.createElement('h2');
    heading.classList.add('news__heading');
    heading.innerHTML = newsTitle;
    
    const date = document.createElement('h4');
    heading.classList.add('news__date');
    date.innerHTML = newsDate;


    const description = document.createElement('p');
    description.classList.add('news__description');
    description.innerHTML = newsDescription;
    

    parent.appendChild(heading);
    parent.appendChild(date);
    parent.appendChild(description);

    return parent;
}


const appendComponent = async () => {
    const container = document.querySelector('.news__container');
    const response = await fetchNews(newsNumber);
    // console.table(response)
    for (news of response) {
        const newsComponent = createComponent(news.title, news.date, news.description);
        container.appendChild(newsComponent);
    }

}


const fetchMore = document.querySelector('.fetch').addEventListener('click', function() {
    newsNumber++;
    appendComponent();
})



window.onload = function() {
    
    appendComponent().then(() => document.body.style = "visibility: visible;");
}