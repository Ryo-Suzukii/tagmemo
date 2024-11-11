<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue';

function createStars() {
  const starryBg = document.querySelector('.starry-bg');
  if (!starryBg) return;

  // 通常の星を作成
  for (let i = 0; i < 200; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = `${Math.random() * 100}%`;
    star.style.top = `${Math.random() * 100}%`;
    star.style.width = `${Math.random() * 3}px`;
    star.style.height = star.style.width;
    star.style.animationDelay = `${Math.random() * 2}s`;
    starryBg.appendChild(star);
  }
}

function createShootingStar() {
  const starryBg = document.querySelector('.starry-bg');
  if (!starryBg) return;

  const shootingStar = document.createElement('div');
  shootingStar.className = 'shooting-star';
  
  shootingStar.style.left = `${Math.random() * 100}%`;
  shootingStar.style.top = `${Math.random() * 20}%`;
  
  starryBg.appendChild(shootingStar);

  shootingStar.addEventListener('animationend', () => {
    shootingStar.remove();
  });
}

let shootingStarInterval: number;

onMounted(() => {
  createStars();
  
  const createRandomShootingStar = () => {
    createShootingStar();
    const nextInterval = 5000 + Math.random() * 10000;
    shootingStarInterval = window.setTimeout(createRandomShootingStar, nextInterval);
  };
  
  createRandomShootingStar();
});

onUnmounted(() => {
  if (shootingStarInterval) {
    clearTimeout(shootingStarInterval);
  }
});
</script>

<template>
  <div class="starry-bg"></div>
</template>
