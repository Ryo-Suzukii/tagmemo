<template>
  <canvas ref="canvas" class="starry-background"></canvas>
</template>

<script lang="ts">
export default {
  mounted() {
    this.createStarryAnimation();
  },
  methods: {
    createStarryAnimation() {
      const canvas = this.$refs.canvas as HTMLCanvasElement;
      const ctx = canvas.getContext("2d");
      if (!ctx) {
        console.error("Failed to get 2D context");
        return;
      }
      let width = window.innerWidth;
      let height = window.innerHeight;
      canvas.width = width;
      canvas.height = height;

      const stars = Array(200).fill({}).map(() => ({
        x: Math.random() * width,
        y: Math.random() * height,
        size: Math.random() * 2 + 1,
        speed: Math.random() * 0.5 + 0.2,
        alpha: Math.random(),
      }));

      function drawStars() {
        if (ctx) {
          ctx.clearRect(0, 0, width, height);
        }
        stars.forEach(star => {
          if (ctx) {
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(255, 255, 255, ${star.alpha})`;
            ctx.fill();
          }
        });
      }

      function updateStars() {
        stars.forEach(star => {
          star.y += star.speed;
          if (star.y > height) {
            star.y = 0;
            star.x = Math.random() * width;
          }
        });
      }

      function animate() {
        updateStars();
        drawStars();
        requestAnimationFrame(animate);
      }

      animate();

      window.addEventListener("resize", () => {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
      });
    },
  },
};
</script>

<style>
.starry-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}
</style>
