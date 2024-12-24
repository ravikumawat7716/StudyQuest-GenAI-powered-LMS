// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { apiKey, appId, messagingSenderId } from "./config";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration (we have removed our project id , )
const firebaseConfig = {
  apiKey: apiKey,
  authDomain: "paste your auth domain here", // format : projectidxyz.firebaseapp.com
  projectId: "paste your project id here", // format : projectidxyz
  storageBucket: "paste your storage bucket here", // format : projectidxyz.appspot.com
  messagingSenderId: messagingSenderId,
  appId: appId,
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);

// How to generate project id & auth domain , storage bucket
// 1. Go to firebase console , url : https://console.firebase.google.com/
// 2. Create a new project
// 3. Go to project settings
// 4. Click on General tab
// 5. Scroll down to Your apps section
// 6. Click on the web app icon
// 7. Copy the config object and paste it in the firebase.js file
// 8. Copy the project id and paste it in the projectId field
// 9. Copy the auth domain and paste it in the authDomain field
// 10. Copy the storage bucket and paste it in the storageBucket field
// 11. Save the file
// 12. Go to the firebase console
// 13. Click on Authentication tab
// 14. Click on Sign-in method
// 15. Enable the sign-in methods you want to use
// 16. Save the changes
// 17. Go to the firebase console
// 18. Click on Database tab
// 19. Click on Create database
// 20. Select the location
// 21. Click on Done
// 22. Click on the Rules tab

