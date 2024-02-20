<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1 style="text-align: center;">Hotel Rating Classifier</h1>
    <img src="https://www.kayak.co.in/news/wp-content/uploads/sites/76/2023/08/THEME_HOTEL_SIGN_FIVE_STARS_FACADE_BUILDING_GettyImages-1320779330-3.jpg" alt="Header Image">
  <h2>Project Overview</h2>
  <ol>
    <li><strong>Data Loading:</strong> Data is sourced from <a href="https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe">Kaggle</a>.</li>
    <li><strong>Preprocessing:</strong> Handling missing data and outliers.</li>
    <li><strong>Text Data Processing (NLP):</strong> Utilizing Natural Language Processing techniques for text data.</li>
    <li><strong>Modeling:</strong> Employing XGBoost with an accuracy of 88%.</li>
    <li><strong>Transformer Usage:</strong> Implementing a simple transformer to process hotel reviews.</li>
     <li><strong>Deployment:</strong> Using stremlit for deployment.</li>
  </ol>
  <hr>
  <h2 style="color:red; font-size: 25px;">About DataSet🧐🧐</h2><br>
  <p style="color:#5b5b5b; font-size: 18px;"> This dataset contains 515,000 customer reviews and scoring of 1493 luxury hotels across Europe. Meanwhile, the geographical location of hotels are also provided for further analysis.👇👇</p><br>
        <a href="https://www.kaggle.com/datasets/jiashenliu/515k-hotel-reviews-data-in-europe" target="_blank" style="color: #4483b5; font-size: 20px;">👉👉Hotel_dataSet </a>
        <p  style="color:red; font-size: 25px;">Data Content</p>
        <ul style="color:green; font-size: 12px;"   >
         <li id="up">Hotel_Address : Address of hotel</li>
         <li>Review_Date. : Date when reviewer posted the corresponding review.</li>
         <li>Average_Score. :  Average Score of the hotel, calculated based on the latest comment in the last year.</li>
         <li>Hotel_Name : Name of Hotel</li>
         <li>Reviewer_Nationality :Nationality of Reviewer</li>
         <li>Negative_Review. : Negative Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Negative'</li>
         <li>Review_Total_Negative_Word_Counts: Total number of words in the negative review.</li>
         <li>Positive_Review: Positive Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Positive'</li>
         <li>Review_Total_Positive_Word_Counts: Total number of words in the positive review.</li> 
         <li>Reviewer_Score: Score the reviewer has given to the hotel, based on his/her experience</li>
         <li>Total_Number_of_Reviews_Reviewer_Has_Given: Number of Reviews the reviewers has given in the past.</li>             
         <li>Total_Number_of_Reviews: Total number of valid reviews the hotel has.</li>
         <li>Tags: Tags reviewer gave the hotel.</li>    
         <li>days_since_review: Duration between the review date and scrape date.</li>
         <li>Additional_Number_of_Scoring: There are also some guests who just made a scoring on the service rather than a review. This number indicates how many valid scores without review in there.</li>   
         <li>lat: Latitude of the hotel</li>   
         <li>lng: longtitude of the hotel</li>   
        </ul>
</body>
</html>

