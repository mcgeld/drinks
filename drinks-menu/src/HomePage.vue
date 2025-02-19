<template>
  <div class="home">
    <h1 class="title">Welcome to the Bar</h1>

    <!-- Tab Navigation (Future Feature) -->
    <div class="tabs">
      <button @click="activeTab = 'featured'" :class="{ active: activeTab === 'featured' }">Featured</button>
      <button @click="activeTab = 'all'" :class="{ active: activeTab === 'all' }">All Drinks</button>
      <button @click="activeTab = 'custom'" :class="{ active: activeTab === 'custom' }">Create Your Own</button>
    </div>

    <!-- Tab Content -->
    <div v-if="activeTab === 'featured'">
      <p>Featured drinks coming soon!</p>
    </div>
    <div v-if="activeTab === 'all'">
      <DrinkMenu />
    </div>
    <div v-if="activeTab === 'custom'">
      <p>Custom drink builder coming soon!</p>
    </div>

    <!-- Sign In / Sign Up -->
    <div class="auth-section">
      <p>Sign in to save your drinks & preferences.</p>
      <button class="auth-button">Sign In</button>
      <button class="auth-button">Sign Up</button>
    </div>
  </div>
</template>

<script>
import DrinkMenu from "@/components/DrinkMenu.vue"; // Import the menu component

export default {
  components: { DrinkMenu },
  data() {
    return {
      activeTab: "all", // Default tab
    };
  },
};
</script>

<style scoped>
.home {
  text-align: center;
  padding: 20px;
}

.title {
  font-size: 2em;
}

.tabs {
  margin-bottom: 20px;
}

.tabs button {
  padding: 10px 20px;
  margin: 5px;
  border: none;
  background-color: #ddd;
  cursor: pointer;
  font-size: 16px;
}

.tabs button.active {
  background-color: #4CAF50;
  color: white;
}

.auth-section {
  margin-top: 20px;
}

.auth-button {
  margin: 5px;
  padding: 10px 20px;
  border: none;
  background-color: #007BFF;
  color: white;
  cursor: pointer;
}

.auth-button:hover {
  background-color: #0056b3;
}
</style>
