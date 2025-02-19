<template>
  <div>
    <h1>Drink Menu</h1>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <div v-for="drink in drinks" :key="drink.id" class="drink-card">
        <h2>{{ drink.name }}</h2>
        <img :src="drink.image_url" alt="Drink Image" />
        <p>{{ drink.description }}</p>
        <button @click="orderDrink(drink.id)">Order</button>
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
      ordering: false, // New state for tracking order status
      message: "" // To show order confirmation
    };
  },
  methods: {
    async fetchDrinks() {
      try {
        const response = await fetch(`${apiUrl}/drinks`);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        this.drinks = await response.json();
        this.loading = false;
      } catch (error) {
        console.error("Error fetching drinks:", error);
      }
    },

    orderDrink(drinkId) {
      /*let userId = localStorage.getItem("userId");
      let coasterId = localStorage.getItem("coasterId");*/

      let userId = 1;
      let coasterId = 1;

      fetch("/api/orders", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ drink_id: drinkId, user_id: userId, coaster_id: coasterId }),
      })
      .then(response => response.json())
      .then(data => {
        console.log("Order response:", data); //Debugging output
        if (!userId) {
          // First time ordering, save the guest user ID
          localStorage.setItem("userId", data.user_id);
        }
        alert("Order placed!");
      })
      .catch(error => console.error("Error placing order:", error));
    }

  },
  mounted() {
    this.fetchDrinks();
  }
};
</script>

<style>
body { font-family: Arial, sans-serif; text-align: center; }
.drink-card { border: 1px solid #ddd; border-radius: 10px; padding: 10px; max-width: 300px; margin: 10px auto; }
img { width: 100%; border-radius: 10px; }
button { background-color: #28a745; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer; width: 100%; }
</style>

