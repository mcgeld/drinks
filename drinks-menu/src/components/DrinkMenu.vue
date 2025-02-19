<template>
  <div>
    <h1 class="title">Drink Menu</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else class="menu">
      <div 
        v-for="drink in drinks" 
        :key="drink.id" 
        class="drink-card"
        @click="goToDrink(drink.id)"
      >
        <img :src="drink.image_url" alt="Drink Image" class="drink-image"/>
        <div class="drink-info">
          <h2>{{ drink.name }}</h2>
          <p>{{ drink.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const apiUrl = process.env.VUE_APP_API_URL;

export default {
  data() {
    return {
      drinks: [],
      loading: true,
    };
  },
  methods: {
    async fetchDrinks() {
      try {
        const response = await fetch(`${apiUrl}/drinks`);
        if (!response.ok) throw new Error("Failed to fetch drinks");
        this.drinks = await response.json();
      } catch (error) {
        console.error("Error fetching drinks:", error);
      } finally {
        this.loading = false;
      }
    },
    goToDrink(drinkId) {
      this.$router.push(`/drink/${drinkId}`);
    }
  },
  mounted() {
    this.fetchDrinks();
  }
};
</script>

<style scoped>
.title {
  text-align: center;
}

.menu {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: center;
}

.drink-card {
  width: 200px;
  border-radius: 10px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s;
  background: white;
  padding: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.drink-card:hover {
  transform: scale(1.05);
}

.drink-image {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 5px;
}

.drink-info {
  padding: 10px;
}
</style>
