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

    <!-- Coaster ID Confirmation Modal -->
    <div v-if="showCoasterPrompt" class="modal">
      <div class="modal-content">
        <h2>Confirm or Update Coaster ID</h2>
        <input v-model="coasterId" type="number" placeholder="Enter Coaster ID" />
        <button @click="placeOrder">Confirm & Order</button>
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
      showCoasterPrompt: false,
      coasterId: localStorage.getItem("coasterId") || "",
      currentDrinkId: null,
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
      this.$router.push({ name: "DrinkDetail", params: { id: drinkId }});
    },
    confirmCoaster(drinkId) {
      this.currentDrinkId = drinkId;
      this.showCoasterPrompt = true; // Show the modal before placing an order
    },
    placeOrder() {
      if (!this.coasterId) {
        alert("Please enter your coaster ID before ordering!");
        return;
      }

      localStorage.setItem("coasterId", this.coasterId);

      fetch(`${apiUrl}/orders`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: null, drink_id: this.currentDrinkId, coaster_id: this.coasterId }),
      })
        .then(response => response.json())
        .then(data => console.log("Order placed:", data))
        .catch(error => console.error("Error placing order:", error));

      this.showCoasterPrompt = false;
    },
  },
  mounted() {
    this.fetchDrinks();
  }
};
</script>

<style scoped>
/* Modal Styling */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
}

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
