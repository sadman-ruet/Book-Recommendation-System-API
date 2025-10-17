---
title: Book Recommendation API
emoji: 📚
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "0.0.1"
app_file: app.py
pinned: false
---
# **Book Recommendation System API**

This project is a **Book Recommendation System API** built using **FastAPI** and integrates with external APIs like Google and Pinecone for recommendation functionalities.

---

## **Setup Instructions**

### 1. **Create a `.env` File**

Create a `.env` file in the root directory of your project and add the following lines with your actual API keys:

```bash
GOOGLE_API_KEY=<Your_Google_API_Key>
PINECONE_API_KEY=<Your_Pinecone_API_Key>
MONGO_URI=<Your_MongoDB_Connection_String>
```

Replace `<Your_Google_API_Key>`,`<Your_MongoDB_Connection_String>` and `<Your_Pinecone_API_Key>`  with the respective API keys/Connection String  you have.

---

### 2. **Install Dependencies**

Make sure you have all the required libraries installed. You can install them using `pip` and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

### 3. **Run the API Server**

To start the API server, use **Uvicorn** (an ASGI server for FastAPI) by running this command from the root directory:

```bash
uvicorn app:app --reload
```

This will start the server in development mode with automatic reloads.

---

## **API Testing**

To test the API, follow the steps below:
- ![Query](./images/query.png)
- ![Response](./images/response.png)

---

## **Database**

The application utilizes a database for storing and retrieving data. Here's the relevant structure or diagram:
- - ![Database](./images/database.png)

---

## **Contributing**

If you'd like to contribute to the project, feel free to fork this repository, make changes, and create a pull request.

---

## **License**

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**

- FastAPI for building the API.
- Google and Pinecone for providing powerful API services for recommendations.

---

Let me know if you'd like to add more specific instructions or further details!
