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
        document.getElementById('signInButton').innerText = 'Sign Out';
        document.getElementById('form').style.display = '';
        } else {
        // No user is signed in.
        document.getElementById('signInButton').innerText = 'Sign In with Google';
        document.getElementById('form').style.display = 'none';
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
        window.alert(`Welcome ${result.user.displayName}!`);
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
        .then(result => {})
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

// FirebaseUI config.
var uiConfig = {
  callbacks: {
    signInSuccessWithAuthResult: function(authResult, redirectUrl) {
      var user = authResult.user;
      var userId = user.uid;  // Get the user ID from the user object
      var credential = authResult.credential;
      var isNewUser = authResult.additionalUserInfo.isNewUser;
      var providerId = authResult.additionalUserInfo.providerId;
      var operationType = authResult.operationType;
  
      // Store the user ID in the Flask session object
      fetch('/store_user_id', {
        method: 'POST',
        body: JSON.stringify({'user_id': userId}),
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(function(response) {
        // Redirect to the image upload page
        window.location.assign('/search');
      });
  
      // Return false to prevent automatic redirect
      return false;
    },
    signInFailure: function(error) {
      // Some unrecoverable error occurred during sign-in.
      // Return a promise when error handling is completed and FirebaseUI
      // will reset, clearing any UI. This commonly occurs for error code
      // 'firebaseui/anonymous-upgrade-merge-conflict' when merge conflict
      // occurs. Check below for more details on this.
      return handleUIError(error);
    },
    uiShown: function() {
      // The widget is rendered.
      // Hide the loader.
      document.getElementById('loader').style.display = 'none';
    }
  },
  credentialHelper: firebaseui.auth.CredentialHelper.NONE,
  // Query parameter name for mode.
  queryParameterForWidgetMode: 'mode',
  // Query parameter name for sign in success url.
  queryParameterForSignInSuccessUrl: 'signInSuccessUrl',
  // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
  signInFlow: 'popup',
  signInSuccessUrl: '/search',
  signInOptions: [
    // Leave the lines as is for the providers you want to offer your users.
    firebase.auth.GoogleAuthProvider.PROVIDER_ID,
    {
      provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
      // Whether the display name should be displayed in the Sign Up page.
      requireDisplayName: true
    },
    // firebaseui.auth.AnonymousAuthProvider.PROVIDER_ID // THIS IS THE ANONYMOUS LOGIN
  ],
  // Set to true if you only have a single federated provider like
  // firebase.auth.GoogleAuthProvider.PROVIDER_ID and you would like to
  // immediately redirect to the provider's site instead of showing a
  // 'Sign in with Provider' button first. In order for this to take
  // effect, the signInFlow option must also be set to 'redirect'.
  immediateFederatedRedirect: false,
  // tosUrl and privacyPolicyUrl accept either url string or a callback
  // function.
  // Terms of service url/callback.
  tosUrl: '<your-tos-url>',
  // Privacy policy url/callback.
  privacyPolicyUrl: function() {
    window.location.assign('<your-privacy-policy-url>');
  }
};

var ui = new firebaseui.auth.AuthUI(firebase.auth());
// The start method will wait until the DOM is loaded.
ui.start('#firebaseui-auth-container', uiConfig);