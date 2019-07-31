# Test Burrows-Wheeler transform
def computeBWT(s):
    s = s +'$'
    rows = sorted(s[i:] + s[:i] for i in range(len(s)))
    bwt = [row[-1:] for row in rows]
    print("".join(bwt))
    return "".join(bwt)



computeBWT('I_am_fully_convinced_that_species_are_not_immutable;'
           '_but_that_those_belonging_to_what_are_called_the_same_genera'
           '_are_lineal_descendants_of_some_other_and_generally_extinct_species,'
           '_in_the_same_manner_as_the_acknowledged_varieties_of_any_one_species'
           '_are_the_descendants_of_that_species.'
           '_Furthermore,_I_am_convinced_that_natural_selection_has_been_the_most'
           '_important,_but_not_the_exclusive,_means_of_modification.')

def decodeBWT(r):
    rows = [""] * len(r)
    for i in range(len(r)):
        rows = sorted(r[i] + rows[i] for i in range(len(r)))
    s = [row for row in rows if row.endswith("$")][0]
    print(s.rstrip("$").strip())
    return s.rstrip("$").strip()
decodeBWT('.uspe_gexr_______$..,e.orrs,sdddeedkdsuoden-tf,'
          'tyewtktttt,sewteb_ce__ww__h_PPsm_u_naseueeennnrr'
          'lmwwhWcrskkmHwhttv_no_nnwttzKt_l_ocoo_be___aaaooaAakiiooett_oooi'
          '_sslllfyyD__uouuueceetenagan___rru_aasanIiatt__c__saacooor_ootjeae'
          '______ir__a')







