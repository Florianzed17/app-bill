// Récupérer les éléments du formulaire
const form = document.getElementById('login-form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');

// Écouter l'événement de soumission du formulaire
form.addEventListener('submit', (event) => {
  event.preventDefault(); // Empêcher le formulaire de se soumettre

  // Récupérer les valeurs des champs d'entrée
  const username = usernameInput.value.trim();
  const password = passwordInput.value.trim();

  // Vérifier si les champs sont vides
  if (!username || !password) {
    alert('Veuillez remplir tous les champs!');
    return;
  }

  // Vérifier les informations de connexion
  if (username === 'email' && password === 'mdp') {
    // Rediriger vers la page souhaitée après la connexion réussie
    window.location.href = 'templates/index.html';
  } else {
    alert('Nom d\'utilisateur ou mot de passe incorrect!');
  }
});
