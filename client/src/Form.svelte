<script>
  function isDisabled() {}
</script>

<form action="" class="form">
  <label for="pass_length">Password Length</label>
  <input type="number" name="pass_length" id="pass_length" value="8" />
  <br />
  <small>Your password must be at least 8 characters long</small>

  <div class="form-group">
    <label class="check-label" for="">Has Numbers?</label>
    <select name="has_numbers" id="hasNumbers">
      <option value="yes">Yes</option>
      <option value="no">No</option>
    </select>
  </div>

  <div class="form-group">
    <label class="check-label" for="">Has Special Characters?</label>
    <select name="has_numbers" id="hasNumbers">
      <option value="yes">Yes</option>
      <option value="no">No</option>
    </select>
  </div>

  <input type="submit" value="SUBMIT" />
</form>

<style>
  form {
    width: 85%;
    margin: 8px auto;
  }

  input {
    width: 100%;
    margin: 8px auto;
    border-radius: 5px;
  }

  small {
    text-align: left;
    padding: 8px 0;
    width: 100%;
  }

  .form-group {
    padding: 8px;
  }
  select {
    border-radius: 5px;
    width: 15%;
    letter-spacing: 3px;
  }

  .check-label {
    text-align: left;
    padding: 4px;
  }

  input[type="submit"] {
    background-color: #ff3e00;
    color: white;
    border: none;
    letter-spacing: 8px;
  }
  input[type="submit"]:disabled {
    color: white;
    background-color: slategray;
  }
</style>
