let naloga1 vsebina_datoteke =
  let mass_list = String.split_on_char '\n' (String.trim vsebina_datoteke) in
  (* String.split_on_char : char -> string -> string list *)
  (* String.trim : string -> string *)

  let rec aux acc_fuel = function
  | [] -> acc_fuel
  | mass :: masses ->
    let fuel = int_of_string mass / 3 - 2 in
    aux (acc_fuel + fuel) masses
  in

  string_of_int (aux 0 mass_list)
;;

let naloga2 vsebina_datoteke =
  let rec aux fuel_povecuje mass_zmanjsuje =
  match mass_zmanjsuje with
  | mass when mass / 3 - 2 > 0 ->
    let fuel = mass / 3 - 2 in
    aux (fuel_povecuje + fuel) fuel
  | _ -> fuel_povecuje
  in
  
  let mass_list = String.split_on_char '\n' (String.trim vsebina_datoteke) in
  let mass_list = List.map int_of_string mass_list in

  string_of_int (List.fold_left aux 0 mass_list)
;;


let _ =
  let day = "2019_0" in

  let preberi_datoteko ime_datoteke =
    let chan = open_in ime_datoteke in
    let vsebina = really_input_string chan (in_channel_length chan) in
    close_in chan;
    vsebina
  and izpisi_datoteko ime_datoteke vsebina =
    let chan = open_out ime_datoteke in
    output_string chan vsebina;
    close_out chan
  in

  let vsebina_datoteke = preberi_datoteko ("day_" ^ day ^ ".in") in
  let odgovor1 = naloga1 vsebina_datoteke
  and odgovor2 = naloga2 vsebina_datoteke
  in

  izpisi_datoteko ("day_" ^ day ^ "_1.out") odgovor1;
  izpisi_datoteko ("day_" ^ day ^ "_2.out") odgovor2
;;