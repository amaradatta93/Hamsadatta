import { TestBed } from '@angular/core/testing';

import { SearchfetchService } from './searchfetch.service';

describe('SearchfetchService', () => {
  let service: SearchfetchService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SearchfetchService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
