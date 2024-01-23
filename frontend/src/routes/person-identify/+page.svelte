<script lang="ts">
  import { writable } from 'svelte/store';

  const formData = writable({
      name: '',
      first_name: '',
      last_name: '',
      middle_name: '',
      location: '',
      street_address: '',
      locality: '',
      region: '',
      country: '',
      postal_code: '',
      company: '',
      school: '',
      phone: '',
      email: '',
      email_hash: '',
      profile: '',
      linkedin: '',
      birth_date: ''
  });

  async function handleSubmit() {
      const response = await fetch('/api/person_identify', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify($formData)
      });

      if (response.ok) {
          const result = await response.json();
          console.log(result);
          // Handle the success response
      } else {
          console.error(`Error: ${response.status} ${response.statusText}`);
          // Handle the error response
      }
  }
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="text" bind:value={$formData.name} placeholder="Name"/>
  <input type="text" bind:value={$formData.first_name} placeholder="First Name"/>
  <input type="text" bind:value={$formData.last_name} placeholder="Last Name"/>
  <input type="text" bind:value={$formData.middle_name} placeholder="Middle Name"/>
  <input type="text" bind:value={$formData.location} placeholder="Location"/>
  <input type="text" bind:value={$formData.street_address} placeholder="Street Address"/>
  <input type="text" bind:value={$formData.locality} placeholder="Locality"/>
  <input type="text" bind:value={$formData.region} placeholder="Region"/>
  <input type="text" bind:value={$formData.country} placeholder="Country"/>
  <input type="text" bind:value={$formData.postal_code} placeholder="Postal Code"/>
  <input type="text" bind:value={$formData.company} placeholder="Company"/>
  <input type="text" bind:value={$formData.school} placeholder="School"/>
  <input type="tel" bind:value={$formData.phone} placeholder="Phone"/>
  <input type="email" bind:value={$formData.email} placeholder="Email"/>
  <input type="text" bind:value={$formData.email_hash} placeholder="Email Hash"/>
  <input type="text" bind:value={$formData.profile} placeholder="Profile"/>
  <input type="text" bind:value={$formData.linkedin} placeholder="LinkedIn"/>
  <input type="text" bind:value={$formData.birth_date} placeholder="Birth Date"/>
  <button type="submit">Submit</button>
</form>

<style>
  /* Add your styling here */
</style>