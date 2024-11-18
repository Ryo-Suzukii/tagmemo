<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue';

function createStars() {
  const starryBg = document.querySelector('.starry-bg');
  if (!starryBg) return;

  const orionBasePoint = {
    left: 10,
    top: 10,
  }
  const orionPoints = [
    {left: `${orionBasePoint.left + 0}%`, top: `${orionBasePoint.top + 0}%`, width: '5px', animationDelay: `${Math.random() * 2}s`},
    {left: `${orionBasePoint.left + 9}%`, top: `${orionBasePoint.top + 1}%`, width: '4px', animationDelay: `${Math.random() * 2}s`},
    {left: `${orionBasePoint.left + 4}%`, top: `${orionBasePoint.top + 13}%`, width: '3px', animationDelay: `${Math.random() * 2}s`},
    {left: `${orionBasePoint.left + 5}%`, top: `${orionBasePoint.top + 12.5}%`, width: '3px', animationDelay: `${Math.random() * 2}s`},
    {left: `${orionBasePoint.left + 6}%`, top: `${orionBasePoint.top + 12}%`, width: '3px',  animationDelay: `${Math.random() * 2}s`},
    {left: `${orionBasePoint.left + 8}%`, top: `${orionBasePoint.top + 15}%`, width: '2px', animationDelay: `${Math.random() * 2}s`},
    {left: `${orionBasePoint.left + 2}%`, top: `${orionBasePoint.top + 23}%`, width: '2px', animationDelay: `${Math.random() * 2}s`},
    {left: `${orionBasePoint.left + 10}%`, top: `${orionBasePoint.top + 21}%`, width: '4px', animationDelay: `${Math.random() * 2}s`},
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
