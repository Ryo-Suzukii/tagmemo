<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue';

function createStars() {
  const starryBg = document.querySelector('.starry-bg');
  if (!starryBg) return;

  const orionPoints = [
    {left: '20%', top: '10%', width: '5px', animationDelay: `${Math.random() * 2}s`},
    {left: '29%', top: '11%', width: '4px', animationDelay: `${Math.random() * 2}s`},
    {left: '24%', top: '23%', width: '3px', animationDelay: `${Math.random() * 2}s`},
    {left: '25%', top: '22.5%', width: '3px', animationDelay: `${Math.random() * 2}s`},
    {left: '26%', top: '22%', width: '3px',  animationDelay: `${Math.random() * 2}s`},
    {left: '28%', top: '25%', width: '2px', animationDelay: `${Math.random() * 2}s`},
    {left: '22%', top: '33%', width: '2px', animationDelay: `${Math.random() * 2}s`},
    {left: '30%', top: '31%', width: '4px', animationDelay: `${Math.random() * 2}s`},
  ]
  for (let i = 0; i < 200; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = `${Math.random() * 100}%`;
    star.style.top = `${Math.random() * 100}%`;
    star.style.width = `${Math.random() * 3}px`;
    star.style.height = star.style.width;
    star.style.animationDelay = `${Math.random() * 2}s`;
    const colors = ['white', 'white' ,'red', 'yellow'];
    star.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    starryBg.appendChild(star);
  }
  for (const point of orionPoints) {
    const star = document.createElement('div');
    star.className = 'star orion-point';
    star.style.left = point.left;
    star.style.top = point.top;
    star.style.width = point.width;
    star.style.height = point.width;
    star.style.animationDelay = point.animationDelay;
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
