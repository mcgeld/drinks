<template>
  <div v-if="drink" class="drink-detail">
    <img :src="drink.image_url" alt="Drink Image" class="drink-image" />
    <h1>{{ drink.name }}</h1>
    <p>{{ drink.description }}</p>
    <p>Price: {{ drink.price ? `$${drink.price.toFixed(2)}` : "N/A" }}</p>

    <button @click="showCoasterEntry = true" class="order-button">Order This Drink</button>
    <!-- Coaster Entry Modal -->
    <CoasterEntry
        :show="showCoasterEntry"
        @confirm="handleCoaster"
        @close="showCoasterEntry = false"
     />
  </div>
  <div v-else class="loading">Loading...</div>
</template>

<script>
import CoasterEntry from "@/components/CoasterEntry.vue";
const apiUrl = process.env.VUE_APP_API_URL;

export default {
  components: { CoasterEntry },
  data() {
    return {
      drink: {},
      loading: true,
      showCoasterEntry: false,
    };
  },
  methods: {
    handleCoaster(coasterId) {
      this.showCoasterEntry = false;
      this.submitOrder(coasterId);
    },
    submitOrder(coasterId) {
      const userId = localStorage.getItem("userId");
      const parsedUserId = userId && userId !== "undefined" ? parseInt(userId, 10) : null;
      fetch(`${process.env.VUE_APP_API_URL}/orders`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          user_id: parsedUserId,
          coaster_id: coasterId,
          drink_id: this.drink.id,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Order successful!", data);
          alert("Your order has been placed!");
        })
        .catch((error) => console.error("Order failed:", error));
    },
    async fetchDrink() {
      try {
        const response = await fetch(`${apiUrl}/drinks/${this.$route.params.id}`);
        if (!response.ok) throw new Error("Failed to fetch drink details");
        this.drink = await response.json();
      } catch (error) {
        console.error("Error fetching drink details:", error);
      } finally {
        this.loading = false;
      }
    },
  },
  mounted() {
    this.fetchDrink();
  },
};
</script>

<style scoped>
.drink-detail {
  text-align: center;
  padding: 20px;
}

.drink-image {
  width: 100%;
  max-width: 300px;
  height: auto;
  border-radius: 10px;
}

.order-button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px;
}

.order-button:hover {
  background-color: #45a049;
}
</style>

