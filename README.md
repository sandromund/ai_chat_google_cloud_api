# ai_chat_google_cloud_api
Deploy ML Models With Google Cloud Run


# Docker 
````commandline
docker build -t chat-api .
docker run chat-api -p:80:80  

gcloud builds submit --tag gcr.io/chat-ai-405601/index
gcloud run deploy --image gcr.io/chat-ai-405601/index --platform managed
````


https://www.youtube.com/watch?v=vieoHqt7pxo
