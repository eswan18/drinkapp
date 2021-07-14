<template>
  <div>
    <p>{{ msg }}</p>
    <p>{{ currentUserText }}</p>
    <p>{{ currentUser }}</p>
    <button @click="newUser">New User</button>
    <br><br>
    <input v-model="userToBeSet" placeholder="User ID"/>
    <button @click="setUser">Log In</button>
  </div>
</template>

<script>
export default {
  name: 'Drinks',
  data() {
    return {
      msg: 'Hello!',
      currentUser: null,
      userToBeSet: null,
    };
  },
  methods: {
    setUser() {
      fetch(`http://localhost:8000/${this.userToBeSet}`, {
        method: 'GET',
      }).then((response) => {
        if (!response.ok) {
          alert(`Server returned ${response.status}: ${response.statusText}`);
        }
        return response.json();
      }).then((response) => {
        this.currentUser = this.userToBeSet;
        this.username = response.username;
      }).catch((err) => {
        console.log(err);
      });
    },
    newUser() {
      alert('new');
    },
  },
  computed: {
    currentUserText() {
      let text;
      if (this.currentUser) {
        text = `Current user ${this.currentUser}`;
      } else {
        text = 'No user logged in';
      }
      return text;
    },
  },
};
</script>
