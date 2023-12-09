const config = {
    apiKey: "AIzaSyAO3zQajGJU0Cw3t7S9u7Qyt0aREro-42A",
    authDomain: "se-firebase-b3664.firebaseapp.com",
    projectId: "se-firebase-b3664",
    storageBucket: "se-firebase-b3664.appspot.com",
    messagingSenderId: "415249616254",
    appId: "1:415249616254:web:4fde030fc8169178bab72f",
    measurementId: "G-P70CL60GRZ"
    };

    firebase.initializeApp(config);

    // Watch for state change from sign in
    function initApp() {
    firebase.auth().onAuthStateChanged(user => {
        if (user) {
        // User is signed in.
        // document.getElementById('signInButton').innerText = 'Sign Out';
        //document.getElementById('form').style.display = '';
        console.log(`User ${user} is signed in.`);
        } else {
        window.location.assign('/');
        // No user is signed in.
        //document.getElementById('signInButton').innerText = 'Sign In with Google';
        //document.getElementById('form').style.display = 'none';
        console.log(`No user is signed in.`);
        }
    });
    }
    window.onload = function () {
      initApp();
    };

    function signIn() {
    const provider = new firebase.auth.GoogleAuthProvider();
    provider.addScope('https://www.googleapis.com/auth/userinfo.email');
    firebase
        .auth()
        .signInWithPopup(provider)
        .then(result => {
        // Returns the signed in user along with the provider's credential
        console.log(`${result.user.displayName} logged in.`);
        //window.alert(`Welcome ${result.user.displayName}!`);
        })
        .catch(err => {
        console.log(`Error during sign in: ${err.message}`);
        window.alert(`Sign in failed. Retry or check your browser logs.`);
        });
    }

    function signOut() {
    firebase
        .auth()
        .signOut()
        .then(result => {
        // Sign-out successful.
        console.log(`User signed out.`);
        window.alert(`You have been signed out.`);
        window.location.assign('/');
        })
        .catch(err => {
        console.log(`Error during sign out: ${err.message}`);
        window.alert(`Sign out failed. Retry or check your browser logs.`);
        });
    }

    // Toggle Sign in/out button
    function toggle() {
      if (!firebase.auth().currentUser) {
          signIn();
      } else {
          signOut();
      }
    }