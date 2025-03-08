import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

const app = createApp(App);
app.use(router);
app.mount('#app');

const apiUrl = process.env.VUE_APP_API_URL;
const urlParams = new URLSearchParams(window.location.search);
const coasterFromUrl = urlParams.get("coaster");

// Fetch session ID from the API
fetch(`${apiUrl}/sessions/current`)
  .then(response => response.json())
  .then(data => {
    const storedCoasterId = localStorage.getItem("coasterId");
    console.log("Stored Coaster ID:", storedCoasterId);
    const currentSessionId = data?.id;
    const storedSessionId = Number(localStorage.getItem("sessionId"));
    console.log("Current Session ID:", currentSessionId);
    console.log("Stored Session ID:", storedSessionId);

    if (storedSessionId !== currentSessionId) {
      // 🔥 Clear coaster ID if session changed
      console.log("REMOVING COASTER ID");
      localStorage.removeItem("coasterId");
    }

    // Store the new session ID
    localStorage.setItem("sessionId", currentSessionId);

    // Override coaster ID if it came from a QR code
    console.log("Coster From URL:", coasterFromUrl);
    if (coasterFromUrl) {
      console.log("SETTING COASTER ID");
      localStorage.setItem("coasterId", coasterFromUrl);
    }
    const afterCoasterId = localStorage.getItem("coasterId");
    console.log("After Coaster ID:", afterCoasterId);
  })
  .catch(error => console.error("Error fetching session:", error));

