<template>
  <div v-if="show" class="modal-overlay">
    <div class="modal-content">
      <div class="coaster-container">
        <img src="@/assets/coaster-placeholder.png" alt="Coaster" class="coaster-image" />
        <input
          type="text"
          v-model="coasterNumber"
          class="coaster-input"
          maxlength="3"
          readonly
          ref="coasterInput"
        />
      </div>
      <div class="keypad">
        <button v-for="num in keypadNumbers" :key="num" @click="addNumber(num)">{{ num }}</button>
        <button @click="removeNumber">←</button>
      </div>
      <div class="modal-buttons">
        <button class="cancel" @click="closeModal">Cancel</button>
        <button class="confirm" @click="confirmCoaster">Confirm</button>
      </div>
    </div>
  </div>
</template>

<script>
  const apiUrl = process.env.VUE_APP_API_URL;
export default {
  props: ['show'],
  data() {
    return {
      coasterNumber: localStorage.getItem("coasterId") || '',
      hasTyped: false,
      keypadNumbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    };
  },
  mounted() {
    this.$nextTick(() => {
      if (this.$refs.coasterInput) {
        this.$refs.coasterInput.focus();
      }
    });
  },
  methods: {
    addNumber(num) {
      if (!this.hasTyped) {
        this.coasterNumber = '';
        this.hasTyped = true;
      }
      if (this.coasterNumber.length < 3) {
        this.coasterNumber += num;
      }
    },
    removeNumber() {
      this.coasterNumber = this.coasterNumber.slice(0, -1);
    },
    closeModal() {
      this.hasTyped = false;
      this.$emit('close');
    },
    confirmCoaster() {
      if(this.coasterNumber === '') {
        alert("Please enter a coaster number");
        return;
      }
      fetch(`${apiUrl}/coasters/${this.coasterNumber}`)
        .then(response => {
          if (!response.ok) {
            throw new Error("Invalid coaster number.");
          }
          return response.json();
        })
        .then(() => {
          localStorage.setItem("coasterId", this.coasterNumber);
          this.$emit('confirm', this.coasterNumber);
        })
        .catch(error => {
          alert(error.message);
          this.coasterNumber = "";
        });
    }
  }
};
</script>

<style>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.coaster-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.coaster-image {
  width: 100%;  /* Adjust based on your modal size */
  max-width: 200px; /* Set a max width to prevent excessive scaling */
  height: auto; /* Ensures aspect ratio is maintained */
  display: block;
  margin: 0 auto; /* Centers the image */
}

.coaster-input {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 24px;
  width: 60px;
  text-align: center;
  background: rgba(255, 255, 255, 0.8);
  border: none;
  padding: 5px;
  border-radius: 5px;
}

.keypad {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-top: 20px;
}

.keypad button {
  font-size: 24px;
  padding: 15px;
}

.modal-buttons {
  margin-top: 20px;
  display: flex;
  gap: 20px;
  width: 100%;
  justify-content: center;
}

.cancel, .confirm {
  padding: 10px 20px;
  font-size: 18px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
}

.cancel {
  background: red;
  color: white;
}

.confirm {
  background: green;
  color: white;
}
</style>

