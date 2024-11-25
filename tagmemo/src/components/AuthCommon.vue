<script lang="ts">
import { defineComponent } from 'vue';
import { useAuthData } from '../stores/AuthCommon';

export default defineComponent({
  name: 'AuthCommon',
  setup() {
    const authStore = useAuthData();
    return { authStore };
  },
});
</script>
