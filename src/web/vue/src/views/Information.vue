<template>
  <div>
    <h1 class="text-4xl text-gray-900 font-bold mb-6">Informatie</h1>
    <div class="flex mb-10">
      <div class="w-full max-w-prose mr-8">
        <p class="max-w-prose text-gray-700 leading-relaxed">
          <!--Abstract-->
          Het lectoraat Data Intelligence van Zuyd hogeschool zag een kans bij
          het voorspellen van machineonderhoud. Dit product is het gevolg van
          deze interesse van Zuyd hogeschool. Voorafgaan aan de ontwikkel fase
          heeft er een onderzoek plaatsgevonden over welke methodieken mogelijk
          gebruikt konden worden voor het voorspellen van onderhoud. Uit dit
          onderzoek blijkt dat LSTM het beste aansloot aan de gekozen dataset.
          Parallel aan de ontwikkeling is het ontwerp gedocumenteerd, dit is in
          te zien door de verschillende stakeholders.
          <br /><br />
          Binnen deze applicatie is het mogelijk om vroegtijdig te acteren voor
          onderhoud. De applicatie geeft weer wanneer verwacht wordt dat een
          onderdeel (bijna) defect is. Dit gebeurd op basis van een LSTM model.
          De gebruiker kan zelf een model inladen, exporteren of aanmaken binnen
          de applicatie. Tevens heeft de gebruiker de mogelijkheid om de
          betrouwbaarheid/nauwkeurigheid van het model in te zien op basis van
          de verschillende 'target' variabelen. Aan de rechter kant ziet u de
          gehele pipeline van de applicatie. De pipeline geeft weer hoe de
          applicatie is ingedeeld, van begin tot einde. Voor meer informatie
          wordt u verwezen naar de bijgeleverde readme, notebook of u kunt een
          van de ontwikkelaars contacteren.
          <br /><br />
        </p>
      </div>
      <div class="w-full flex justify-center">
        <img
          src="@/assets/pipeline.png"
          alt="Visualisation about pipeline"
          class="rounded shadow-xl h-96"
        />
      </div>
    </div>
    <div>
      <h1 class="text-3xl text-gray-800 font-bold mb-6">Gemaakt door</h1>
      <div class="grid grid-cols-4 gap-8">
        <made-by-member
          name="Giuseppe Collura"
          email="1826689collura@zuyd.nl"
          github="peppe0203"
        />
        <made-by-member
          name="Cédric Cortenraede"
          email="1845675cortenraede@zuyd.nl"
          github="CedricCortenraede"
        />
        <made-by-member
          name="Joey Einerhand"
          email="1823132einerhand@zuyd.nl"
          github="Joey-Einerhand"
        />
        <made-by-member
          name="Lennox Narinx"
          email="1870920narinx@zuyd.nl"
          github="1870920narinx"
        />
      </div>
    </div>
  </div>
</template>

<script>
import MadeByMember from "../components/MadeByMember";
export default {
  name: "Information",
  components: { MadeByMember },
};
</script>

<style scoped></style>
