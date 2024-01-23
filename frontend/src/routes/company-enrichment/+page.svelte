<script lang="ts">
  import { onMount } from 'svelte';
  import { browser } from '$app/environment';

  interface CompanyEnrichmentData {
    pdl_id: string;
    name: string;
    website: string;
    profile: string;
  }

  let formData: CompanyEnrichmentData = {
    pdl_id: '',
    name: '',
    website: '',
    profile: ''
  };

  async function handleSubmit() {
    if (browser) {
      const response = await fetch('http://localhost:8000/company_enrichment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const result = await response.json();
      console.log(result);
    }
  }

  onMount(() => {
    // Initialization logic if needed
  });
</script>

<form on:submit|preventDefault={handleSubmit}>
  <label for="pdl_id">
    PDL ID
    <input type="text" id="pdl_id" bind:value={formData.pdl_id} placeholder="PDL ID of the company (optional)"/>
  </label>

  <label for="name">
    Name
    <input type="text" id="name" bind:value={formData.name} placeholder="Name of the company (optional)"/>
  </label>

  <label for="website">
    Website
    <input type="text" id="website" bind:value={formData.website} placeholder="Company website (optional)"/>
  </label>

  <label for="profile">
    Profile
    <input type="text" id="profile" bind:value={formData.profile} placeholder="Social profile of the company (optional)"/>
  </label>

  <button type="submit">Submit</button>
</form>

<style>
  /* Add your styles here */
</style>