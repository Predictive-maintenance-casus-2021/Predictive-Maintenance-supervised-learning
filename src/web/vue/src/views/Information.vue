<template>
  <div>
    <h1 class="text-4xl text-gray-900 font-bold mb-6">Informatie</h1>
    <div class="flex mb-10">
      <div class="w-full max-w-prose mr-8">
        <p class="max-w-prose text-gray-700 leading-relaxed">
          <!--Abstract-->
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
          fringilla augue vel porta bibendum. Vivamus a mattis dolor. Ut lectus
          orci, tincidunt vel eleifend sollicitudin, varius ut turpis. Curabitur
          vel mi vitae dolor rutrum suscipit. Quisque volutpat nibh leo,
          imperdiet efficitur metus accumsan eget. In commodo risus eu lacus
          rhoncus ultricies. Aenean finibus massa elit. Maecenas placerat, dui
          in gravida sodales, purus tellus pulvinar urna, eget accumsan tortor
          tellus non arcu <br /><br />
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
          fringilla augue vel porta bibendum. Vivamus a mattis dolor. Ut lectus
          orci, tincidunt vel eleifend sollicitudin, varius ut turpis. Curabitur
          vel mi vitae dolor rutrum suscipit. Quisque volutpat nibh leo,
          imperdiet efficitur metus accumsan eget. In commodo risus eu lacus
          rhoncus ultricies. Aenean finibus massa elit. Maecenas placerat, dui
          in gravida sodales, purus tellus pulvinar urna, eget accumsan tortor
          tellus non arcu <br /><br />
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
